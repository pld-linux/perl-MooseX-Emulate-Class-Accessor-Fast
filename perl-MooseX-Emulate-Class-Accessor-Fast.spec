#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MooseX
%define	pnam	Emulate-Class-Accessor-Fast
Summary:	MooseX::Emulate::Class::Accessor::Fast - Emulate Class::Accessor::Fast behavior using Moose attributes
Summary(pl.UTF-8):	MooseX::Emulate::Class::Accessor::Fast - Emuluje zachowanie Class::Accessor::Fast przy użyciu atrybutów Moose
Name:		perl-MooseX-Emulate-Class-Accessor-Fast
Version:	0.00900
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	36ed235d4d2d9759c24a99358eb471e6
URL:		http://search.cpan.org/dist/MooseX-Emulate-Class-Accessor-Fast/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-Moose >= 0.74
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-namespace-clean
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts to emulate the behavior of Class::Accessor::Fast
as accurately as possible using the Moose attribute system. The public
API of Class::Accessor::Fast is wholly supported, but the private
methods are not. If you are only using the public methods (as you
should) migration should be a matter of switching your use base line
to a with line.

%description -l pl.UTF-8
Moduł ten próbuje naśladować zachowanie Class::Accessor::Fast tak
dokładnie jak to możliwe przy użyciu systemu atrybutu Moose. Publiczny
interfejs API do Class::Accessor::Fast jest obsługiwana w całości, ale
metody nie są prywatne. Jeśli używane są tylko metody publiczne
migracji powinna być sprawna.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/Emulate/Class/Accessor/*.pm
%{perl_vendorlib}/MooseX/Emulate/Class/Accessor/Fast
%{_mandir}/man3/*
